from src.database.utils import get_all_models


def test_models_comments():
    all_models = get_all_models()
    for table_schema_name, model_obj in all_models.items():
        list_model = []
        for col in model_obj().__table__.columns:
            if not col.comment:
                raise ValueError(f"col '{col.name}' on table '{model_obj().__table__.name}' does not have comment")
            else:
                list_model.append(len(col.comment) > 0)
        assert all(list_model), f"check all column comments on '{table_schema_name}'"
