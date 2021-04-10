from graphql_relay.node.node import from_global_id

# Functions utils


def transform_global_ids(**kwargs: dict) -> dict:
    """
    Transforma el id de base 64 de GraphQL
    al id de la base de datos relacional
    """
    for key, value in kwargs.items():
        if key.endswith('id'):
            kwargs.update({key: from_global_id(kwargs.get(key))[1]})
    return kwargs


def delete_attributes_none(**kwargs: dict) -> dict:
    """Elimina atributos nulos"""
    kwargs = {key: value for key, value in kwargs.items() if value is not None}
    return kwargs
