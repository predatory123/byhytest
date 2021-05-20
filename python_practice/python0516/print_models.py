# #print_models.py
# unprinted_desians = ['iphone case','robot','robot pendant','dodecahedron']
# complate_models = []
# while unprinted_desians:
#     current_designs = unprinted_desians.pop()
#     print('Printing model: '+ current_designs)
#     complate_models.append(current_designs)
# print('\nThe following models have been printed:')
# for complate_model in complate_models:
#     print(complate_model)
from printing_funcations import *
# def print_models(unprinted_designs,complate_models):
#     while unprinted_designs:
#         current_deaign = unprinted_designs.pop()
#         print('Printing model:'+current_deaign)
#         complate_models.append(current_deaign)
# def show_complate_models(complate_models):
#     print('\nThe following models have been printed:')
#     for complate_model in complate_models:
#         print(complate_model)

unprinted_desians = ['iphone case', 'robot', 'robot pendant', 'dodecahedron']
complate_models = []
print_models(unprinted_desians,complate_models)
show_complate_models(complate_models)


