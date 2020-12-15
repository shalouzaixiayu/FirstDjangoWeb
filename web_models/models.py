from django.db import models


# Create your models here.
class position(models.Model):
    """
    关于英雄的定位字段， 作为搜索条件之一
    """

    class Meta:
        verbose_name_plural = "英雄定位"

    # position_choose = (
    #     ("1", "坦克"),
    #     ("2", "战士"),
    #     ("3", "法师"),
    #     ("4", "刺客"),
    #     ("5", "射手"),
    #     ("6", "辅助"),
    # )
    position_id = models.IntegerField(verbose_name="英雄定位id", default=1, primary_key=True)
    position_name = models.CharField(unique=True, blank=True,
                                     db_index=True, verbose_name="定位", max_length=32)

    def __str__(self):
        return self.position_name


class gender(models.Model):
    """
    英雄的性别定位
    """

    class Meta:
        verbose_name_plural = "英雄性别"

    # gender_choose = (
    #     ("1", "男性"),
    #     ("2", "女性"),
    # )
    gender_id = models.IntegerField(verbose_name="性别id", default=1, primary_key=True)
    gender_fix = models.CharField(db_index=True, unique=True, blank=True
                                  , verbose_name="性别", max_length=32)

    def __str__(self):
        return self.gender_fix


class hero(models.Model):
    """
    英雄的字段介绍
    """

    class Meta:
        verbose_name_plural = "英雄"

    name = models.CharField(max_length=128, verbose_name="英雄姓名")
    hero_gender = models.ForeignKey(gender, related_name="hero_gender",
                                    on_delete=models.CASCADE,
                                    default='1', verbose_name="英雄性别", )
    hero_position = models.ForeignKey(position, related_name="hero_position", on_delete=models.CASCADE, default='1',
                                      verbose_name="英雄定位")
    name_price = models.IntegerField(verbose_name="英雄价格")
    name_describe = models.TextField(verbose_name="英雄介绍")

    def __str__(self):
        return self.name
