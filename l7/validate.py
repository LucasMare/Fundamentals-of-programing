class ValidationError(Exception):
    pass

class Validation:
    @staticmethod
    def validate_person_name(name:str):
        errors = []
        if not name:
            errors.append("Name cannot be empty")

        if errors:
            raise ValidationError(f"{", ".join(errors)}!")

    @staticmethod
    def validate_id_uniqueness(domain_object, repository, message = "ID already present!"):
        if domain_object.id() in repository.ids():
            raise ValidationError(message)

    @staticmethod
    def validate_ids_presence(object_id, repository):
        if object_id not in repository.ids():
            raise ValidationError("ID not in list!")