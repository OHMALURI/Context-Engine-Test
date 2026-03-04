from pymilvus import (
    connections,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
    utility
)

COLLECTION_NAME = "meeting_embeddings"
DIMENSION = 1536  # text-embedding-3-small


def get_collection():
    # Connect to Milvus
    connections.connect(
        alias="default",
        host="localhost",
        port="19530"
    )

    # If collection already exists → load it
    if utility.has_collection(COLLECTION_NAME):
        collection = Collection(COLLECTION_NAME)
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
        description="Meeting transcript embeddings"
    )

    collection = Collection(
        name=COLLECTION_NAME,
        schema=schema
    )

    # Create index for fast search
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