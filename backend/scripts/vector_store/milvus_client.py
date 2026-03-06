from pymilvus import (
    connections,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
    utility
)

DIMENSION = 1536   # text-embedding-3-small


def get_collection(collection_name):
    
    # Connect to Milvus
    connections.connect(
        alias="default",
        host="localhost",
        port="19530"
    )

    # If collection exists → load it
    if utility.has_collection(collection_name):
        collection = Collection(collection_name)
        collection.load()
        return collection

    # Define schema
    fields = [
        FieldSchema(
            name="id",
            dtype=DataType.INT64,
            is_primary=True,
            auto_id=True
        ),
        FieldSchema(
            name="embedding",
            dtype=DataType.FLOAT_VECTOR,
            dim=DIMENSION
        ),
        FieldSchema(
            name="text",
            dtype=DataType.VARCHAR,
            max_length=5000
        )
    ]

    schema = CollectionSchema(
        fields=fields,
        description="Document embeddings"
    )

    collection = Collection(
        name=collection_name,
        schema=schema
    )

    # Create index
    index_params = {
        "metric_type": "L2",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128}
    }

    collection.create_index(
        field_name="embedding",
        index_params=index_params
    )

    collection.load()

    return collection