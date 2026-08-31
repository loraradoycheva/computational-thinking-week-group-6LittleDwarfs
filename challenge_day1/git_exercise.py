import Bao
import Tobit
import David
import Lora
import Rajko
import Tarling

def get_team_members():
    print("This is Team 6 Little Dwarfs. We are:")
    print(Bao.give_bao())
    print(Tobit.give_tobit())
    print(David.give_david())
    print(Lora.give_lora())
    print(Rajko.give_rajko())
    print(Tarling.give_tarling())

def get_story():
    # Act 1
    print(Rajko.act1par1())
    print(Tobit.act1par2())
    print(Bao.act1par3())
    print(Lora.act1par4())
    print(David.act1par5())
    print(Tarling.act1par6())

    # Act 2
    print(Rajko.act2par1())
    print(Tobit.act2par2())
    print(Bao.act2par3())
    print(Lora.act2par4())
    print(David.act2par5())
    print(Tarling.act2par6())

    # Act 3
    print(Rajko.act3par1())
    print(Tobit.act3par2())
    print(Bao.act3par3())
    print(Lora.act3par4())
    print(David.act3par5())
    print(Tarling.act3par6())

if __name__ == "__main__":
    get_team_members()
    get_story()
