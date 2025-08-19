 # lib/owner_pet.py

class Owner:
    """
    Owner has many Pets (one-to-many).
    """
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Owner name must be a non-empty string.")
        self.name = name.strip()

    def pets(self):
        """
        Return a list of Pet instances that belong to this Owner.
        We scan Pet.all to collect those whose owner is self.
        """
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """
        Ensure `pet` is a Pet, then assign this owner to it.
        """
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance.")
        pet.owner = self  # uses Pet.owner setter type-check

    def get_sorted_pets(self):
        """
        Return this owner's pets sorted by pet name (A → Z).
        """
        return sorted(self.pets(), key=lambda p: p.name)


class Pet:
    """
    Pet belongs to one Owner (optional at creation).
    Tracks all Pet instances in Pet.all
    and validates pet_type against PET_TYPES.
    """
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # minimal name validation; tests usually care about type relationships
        if not isinstance(name, str) or not name.strip():
            raise Exception("Pet name must be a non-empty string.")
        self.name = name.strip()

        if pet_type not in Pet.PET_TYPES:
            raise Exception("pet_type must be one of PET_TYPES.")
        self.pet_type = pet_type

        # use property setter to enforce type on owner
        self._owner = None  # internal storage
        if owner is not None:
            self.owner = owner  # triggers type check in setter

        # register instance
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, Owner):
            raise Exception("owner must be an Owner instance or None.")
        self._owner = value

    def __repr__(self):
        owner_name = self.owner.name if self.owner else "No Owner"
        return f"<Pet name={self.name!r} type={self.pet_type!r} owner={owner_name!r}>"
