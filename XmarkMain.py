# import ast
# import astor
#
#
# with open("XmarkSource.py","r") as source:
#     root = ast.parse(source.read())
#     print(astor.dump_tree(root))
#     print("\n")
#
# with open("CollatzSource.py","r") as source:
#     collatzRoot = ast.parse(source.read())
#     print(astor.dump_tree(collatzRoot))
#
# #Embed Collatz Conjecture
# for j in range(5,7):
#     for i in range(2):
#         root.body[j].body.insert(i,collatzRoot.body[i])
#
#     conVar = root.body[j].body[2].test.comparators[0].n
#     body = root.body[j].body[2].body
#
#     #Rewrite "if" node
#     ifNode = ast.If(test=ast.BoolOp(op=ast.And(),values=[ast.Compare(left=ast.BinOp(left=ast.Name(id='x1'), op=ast.Add(), right=ast.Name(id='y1')),ops=[ast.Lt()],comparators=[ast.Num(conVar+2)]),
#                             ast.Compare(left=ast.BinOp(left=ast.Name(id='x1'), op=ast.Sub(), right=ast.Name(id='y1')),ops=[ast.Gt()],comparators=[ast.Num(conVar-2)])]),
#                 body=body,
#                 orelse=[])
#

#     root.body[j].body[2] = ifNode
#
# root = ast.fix_missing_locations(root)
#
# print(astor.dump_tree(root))
#
# with open("XmarkResult.py","w") as source:
#     source.write(astor.to_source(root, indent_with=' ' * 4, add_line_information=False))
#
# print(ast.dump(tree,True,True))
#
#
# class FuncStrLister(ast.NodeVisitor):
#     def visit_If(self, node):
#         if node.lineno == 10:
#             print(astor.dump_tree(node.test.comparators[0].n))
#         self.generic_visit(node)
# 
# FuncStrLister().visit(tree)

# class Rewriteast.Name(ast.NodeTransformer):
#
#     def visit_If(self, node):
#         if node.lineno == 2:
#             return ast.copy_location(ast.If(
#                 test=ast.ast.Compare(left=ast.ast.Num(n=2), ops=[ast.Eq()], comparators=[ast.ast.Num(n=2)]),
#                 body=[ast.Expr(value=ast.Call(func=ast.ast.Name(id='print', ctx=ast.Load()),args=[ast.Str(s='HelloNewWorld')], keywords=[]))],
#                 #orelse=node.orelse)
#                 orelse=[ast.Expr(value=ast.Call(func=ast.ast.Name(id='print', ctx=ast.Load()), args=[ast.Str(s='World')], keywords=[]))])
#     , node)
#         return node
#
# tree = Rewriteast.Name().visit(tree)
# tree = ast.fix_missing_locations(tree)
# #exec(compile(tree,fileast.Name="<ast>",mode="exec"))
#
# with open("AstSource.py","w") as source:
#     source.write(astor.to_source(tree, indent_with=' ' * 4, add_line_information=True))

#Execute this file to watermark the basic prototype

from redbaron import RedBaron

with open('CollatzSource.py', 'r') as file:
    colz1 = RedBaron(file.read())

with open('CollatzSource.py', 'r') as file:
    colz2 = RedBaron(file.read())

colzList = [colz1, colz2]

with open('XmarkInput.py', 'r') as input_file:
    red = RedBaron(input_file.read())

ifNodes = red("if_")

ifNames = ifNodes.map(lambda x: str(x.test.first.value))
ifIndexes = ifNodes.map(lambda x: x.parent.index_on_parent)
ifValues = ifNodes.map(lambda x: int(x.test.second.value))

# Offset insertion
ifIndexes.append(ifIndexes.pop()+1)

#<-----Embed Watermark----->

# Rename
for index, name in enumerate(ifNames):
    test = colzList[0]
    for x in test.find_all('name', value='x'):
        x.value = name
    for y in test.find_all('name', value='y'):
        y.value = 'y' + str(index + 1)
    colzList.pop(0)
    colzList.append(test)

# Populate values
for index, value in enumerate(ifValues):
    test = colzList[index]
    test.find('name', value='v1').value = str(value + 2)
    test.find('name', value='v2').value = str(value - 2)

# Insert
for index, node in enumerate(ifNodes):
    node.replace(colzList[index][1])

# Append
for index, value in enumerate(ifIndexes):
    red.insert(value, colzList[index][0])


with open('XmarkOutput.py', 'w') as dest:
    dest.write(red.dumps())

