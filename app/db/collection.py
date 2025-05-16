from pymilvus import Collection, CollectionSchema, DataType, FieldSchema, connections

connections.connect("default", host="localhost", port=19530)

fields = [
    FieldSchema("id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema("title", dtype=DataType.VARCHAR, max_length=16),
    FieldSchema("text", dtype=DataType.VARCHAR, max_length=128),
    FieldSchema("embedding", dtype=DataType.FLOAT_VECTOR, dim=768),
]

schema = CollectionSchema(fields, description="知识库")

collection = Collection(name="history_zh", schema=schema)
collection.drop()
# collection.create_index(
#     field_name="embedding",
#     index_params={
#         "index_type": "IVF_FLAT",
#         "metric_type": "L2",
#         "params": {"nlist": 128},
#     },
# )
# collection.load()
