from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def str(self):
        return f'{self.name} здоровье: {self.health} урон: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None
        self.__max_health = health  # Максимальное здоровье босса

    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability

    def attack(self, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                if isinstance(hero, Berserk) and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

                # Проверяем, если герой был побежден
                if hero.health <= 0:
                    health_recovered = int(0.15 * (self.__max_health - self.health))
                    self.health += health_recovered
                    if self.health > self.__max_health:
                        self.health = self.__max_health
                    print(f'Босс {self.name} побеждает {hero.name} и восстанавливает {health_recovered} здоровья.')

    @property
    def defence(self):
        return self.__defence

    def str(self):
        return 'BOSS ' + super().str() + f' защита: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        coeff = randint(2, 5)
        boss.health -= coeff * self.damage
        print(f'Воин {self.name} наносит критический урон: {coeff * self.damage}.')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')
        self.__boost_amount = randint(5, 10)

    def apply_super_power(self, boss, heroes_list):
        if self.health <= self.health * 0.4:
            enhanced_boost = int(self.__boost_amount * 1.2)
            for hero in heroes_list:
                hero.damage += enhanced_boost
            print(f'Маг {self.name} усилил урон всех героев на {enhanced_boost} из-за низкого здоровья.')
        else:
            for hero in heroes_list:
                hero.damage += self.__boost_amount
            print(f'Маг {self.name} увеличил урон всех героев на {self.__boost_amount}.')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Берсерк {self.name} вернул {self.__blocked_damage} урона боссу.')

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'SACRIFICE')
        self.__resurrected = False

    def apply_super_power(self, boss, heroes_list):
        if not self.__resurrected:
            for hero in heroes_list:
                if hero.health == 0:
                    hero.health = self.health
                    self.health = 0
                    self.__resurrected = True
                    print(f'Ведьмак {self.name} пожертвовал собой, чтобы оживить {hero.name}.')
                    break


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STEAL_HEALTH')
        self.__round_count = 0

    def apply_super_power(self, boss, heroes_list):
        self.__round_count += 1
        if self.__round_count % 2 == 0:
            stolen_health = randint(10, 20)
            boss.health -= stolen_health
            hero = choice(heroes_list)
            hero.health += stolen_health
            print(f'Хакер {self.name} украл {stolen_health} здоровья у босса и передал его {hero.name}.')


class Golem(Hero):
    def init(self, name, health, damage):
        super().__init__(name, health, damage, 'TANK')

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero != self and hero.health > 0:
                damage_taken = boss.damage // 5
                hero.health -= (boss.damage - damage_taken)
                self.health -= damage_taken
                print(f'Голем {self.name} принял {damage_taken} урона, чтобы защитить {hero.name}.')


class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'INVISIBILITY')
        self.__invisible = False
        self.__rounds_invisible = 0
        self.__stored_damage = 0

    def apply_super_power(self, boss, heroes_list):
        if not self.__invisible:
            self.__invisible = True
            self.__rounds_invisible = 2
            print(f'Аврора {self.name} стала невидимой на 2 раунда.')
        else:
            if self.__rounds_invisible > 0:
                self.__rounds_invisible -= 1
                self.__stored_damage += boss.damage
                print(f'Аврора {self.name} избежала урона в этом раунде.')
            else:
                boss.health -= self.__stored_damage
                print(f'Аврора {self.name} вернула {self.__stored_damage} урона боссу.')
                self.__stored_damage = 0
                self.__invisible = False


# Логика игры и вспомогательные функции
round_number = 0


def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Герои победили!!!')
        return True
    all_heroes_dead = True
    for hero in heroes_list:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Босс победил!!!')
        return True
    return False


def show_statistics(boss, heroes_list):
    print(f' ------------- РАУНД {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)


def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    boss.attack(heroes_list)
    for hero in heroes_list:
        if hero.health > 0:
            hero.apply_super_power(boss, heroes_list)
            hero.attack(boss)
