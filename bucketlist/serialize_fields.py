from flask_restful import fields

item_fields = {
    "item_id": fields.String,
    "item_content": fields.String,
    "done": fields.Boolean,
    "date_created": fields.DateTime(dt_format='rfc822'),
    "date_modified": fields.DateTime(dt_format='rfc822')
}

list_fields = {
    "list_id": fields.String,
    "list_title": fields.String,
    "list_description": fields.String,
    "items": fields.Nested(item_fields),
    "created_by": fields.String,
    "date_created": fields.DateTime(dt_format='rfc822'),
    "date_modified": fields.DateTime(dt_format='rfc822')
}

list_fields_without_items = {
    "list_id": fields.String,
    "list_title": fields.String,
    "list_description": fields.String,
    "created_by": fields.String,
    "date_created": fields.DateTime(dt_format='rfc822'),
    "date_modified": fields.DateTime(dt_format='rfc822')
}
