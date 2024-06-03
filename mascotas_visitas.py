import pandas as pd

mascota = pd.DataFrame(
    data={
        'name': ['Minino', 'Milo', 'Snoopy', 'Blanco', 'LittlePony'],
        'type': ['gato', 'perro', 'perro', 'perro', 'caballo'],
    },
    index=[71,42,11,98,42]
)

visitas = pd.DataFrame(
    data={
        'pet_id': [42, 31, 71, 42, 98, 42],
        'fecha': ['2023-03-15', '2023-03-15', '2023-04-05', '2019-04-06',
                  '2019-04-12', '2024-01-12'],
        'costo': [2000,5000,1000,5000,6000,10000],
    }
)

print(mascota)
print(visitas)

mascota.index.rename('pet_id', inplace=True)
visitas.index.rename('visit_id', inplace=True)

print(mascota)
print(visitas)

print(mascota.query('pet_id==71'))

print(visitas['costo'].sum())
print(visitas['costo'].min())

print(visitas['costo'].max())
print(visitas)

print(visitas.sort_values(by='costo', ascending=False))

tienda=pd.merge(mascota, visitas, how='cross')


print(tienda)
