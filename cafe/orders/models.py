from django.db import models

# Create your models here.


class Order(models.Model):

    status = [

        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),

    ]

    table_number = models.IntegerField(help_text='номер стола')
    items = models.TextField(help_text='список заказанных блюд с ценами(Например борщ 150 , картошка 200 )')
    total_price = models.DecimalField( max_digits=10, decimal_places=2,default=0)
    status = models.CharField(max_length=10, choices=status, default='pending')

    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number} ({self.get_status_display()})"