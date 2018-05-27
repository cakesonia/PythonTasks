from app import ma


class DeviceStructure(ma.Schema):
    class Meta:
        fields = ('id', 'decorationPlace', 'typeOfDecoration', 'color')
