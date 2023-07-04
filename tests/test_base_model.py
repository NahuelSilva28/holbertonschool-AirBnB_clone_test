#!/usr/bin/python3
"""test
"""
from models import storage
from models.base_model import BaseModel


def test_base_model():
    # Cargar objetos previamente guardados
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    # Crear un nuevo objeto
    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)

if __name__ == '__main__':
    test_base_model()
