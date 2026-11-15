from Repository.repository import Repository


class ValidationError(Exception):
    pass

class Validation:
    @staticmethod
    def validate_person_name(name):
        errors = []
        if not name:
            errors.append("Name cannot be empty")

        if errors:
            raise ValidationError(f"{", ".join(errors)}!")

    @staticmethod
    def validate_id_uniqueness(person_or_event, repository):
        if person_or_event.id() in repository.ids():
            raise ValidationError("ID already present!")

    @staticmethod
    def validate_ids_presence(object_id, repository):
        if object_id not in repository.ids():
            raise ValidationError("ID not in list!")