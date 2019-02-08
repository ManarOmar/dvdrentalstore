from rest_framework import serializers
from .models import Actor, Country, Film, Staff, Address, Customer, Store


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('actor_id', 'first_name', 'last_name')


class CountLastNameSerializer(serializers.ModelSerializer):
    last_name_count = serializers.IntegerField()

    class Meta:
        model = Actor
        fields = ('last_name', 'last_name_count')


class Query2Serializer(serializers.ModelSerializer):
    actor_name = serializers.CharField(max_length=90)

    class Meta:
        model = Actor
        fields = ('actor_id', 'actor_name')


class Query6Serializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_id', 'country')


class Query10Serializer(serializers.ModelSerializer):
    film_title = serializers.CharField(max_length=90)
    number_of_actors = serializers.IntegerField()

    class Meta:
        model = Film
        fields = ('film_id', 'film_title', 'number_of_actors')


class Query11Serializer(serializers.ModelSerializer):
    rung_up = serializers.DecimalField(max_digits=8, decimal_places=2)
    rung_month = serializers.IntegerField()

    class Meta:
        model = Staff
        fields = ('staff_id', 'first_name', 'rung_up', 'rung_month')


class Query12Serializer(serializers.ModelSerializer):
    # address_id = serializers.ReadOnlyField(source="address.id")
    # address = serializers.ReadOnlyField(source="address.address")
    staff_address = serializers.CharField(max_length=50)

    class Meta:
        model = Staff
        fields = ('staff_id', 'first_name', 'last_name', 'staff_address')


class Query13Serializer(serializers.ModelSerializer):
    total_paid = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Customer
        fields = ('customer_id', 'last_name', 'total_paid')


class Query14Serializer(serializers.ModelSerializer):
    name_language = serializers.CharField(max_length=20)

    class Meta:
        model = Film
        fields = ('film_id', 'title', 'name_language')


class Query16Serializer(serializers.ModelSerializer):
    country = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)

    class Meta:
        model = Store
        fields = ('store_id', 'country', 'city')


class Query18Serializer(serializers.ModelSerializer):
    frequency_rental = serializers.IntegerField()

    class Meta:
        model = Film
        fields = ('film_id', 'title', 'frequency_rental')


class Query17Serializer(serializers.ModelSerializer):
    amount_of_dollars = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Store
        fields = ('store_id', 'amount_of_dollars')


class Query19Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email')
