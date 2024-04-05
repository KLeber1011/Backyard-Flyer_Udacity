Python 3.13.0a5 (tags/v3.13.0a5:076d169, Mar 12 2024, 21:29:03) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.



import argparse
import time
from enum import Enum

import numpy as np

from udacidrone import Drone
from udacidrone.connection import MavlinkConnection, WebSocketConnection  # noqa: F401
from udacidrone.messaging import MsgID


class Estados(Enum):
    MANUAL = 0
    ARMAMENTO = 1
    DECOLAGEM = 2
    WAYPOINT = 3
    POUSO = 4
    DESARMAMENTO = 5


class BackyardFlyer(Drone):

    def __init__(self, connection):
        super().__init__(connection)
        self.posicao_alvo = np.array([0.0, 0.0, 0.0])
        self.todos_waypoints = []
        self.em_missao = True
        self.verificar_estado = {}

        # estado inicial
        self.estado_voo = Estados.MANUAL

        # TODO: Registre todos os seus callbacks aqui
        self.registrar_callback(MsgID.LOCAL_POSITION, self.callback_posicao_local)
        self.registrar_callback(MsgID.LOCAL_VELOCITY, self.callback_velocidade_local)
        self.registrar_callback(MsgID.STATE, self.callback_estado)

    def callback_posicao_local(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.LOCAL_POSITION` é recebido e self.local_position contém novos dados
        """
        pass

    def callback_velocidade_local(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.LOCAL_VELOCITY` é recebido e self.local_velocity contém novos dados
        """
        pass

    def callback_estado(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.STATE` é recebido e self.armed e self.guided contêm novos dados
        """
        pass

    def calcular_quadrado(self):
        """TODO: Preencha este método
        
        1. Retorna waypoints para voar em um quadrado
        """
        pass

    def transicao_armamento(self):
        """TODO: Preencha este método
        
        1. Assuma o controle do drone
        2. Passe um comando de armamento
        3. Defina a localização inicial como a posição atual
        4. Transição para o estado ARMAMENTO
        """
        print("transição de armamento")

    def transicao_decolagem(self):
        """TODO: Preencha este método
        
        1. Defina a altitude da posição alvo como 3.0m
        2. Comande uma decolagem para 3.0m
        3. Transição para o estado DECOLAGEM
        """
        print("transição de decolagem")

    def transicao_waypoint(self):
        """TODO: Preencha este método
    
        1. Comande a próxima posição de waypoint
        2. Transição para o estado WAYPOINT
        """
        print("transição de waypoint")

    def transicao_pouso(self):
        """TODO: Preencha este método
        
        1. Comande o drone para pousar
        2. Transição para o estado POUSO
        """
        print("transição de pouso")

    def transicao_desarmamento(self):
        """TODO: Preencha este método
        
        1. Comande o drone para desarmar
        2. Transição para o estado DESARMAMENTO
        """
        print("transição de desarmamento")

    def transicao_manual(self):
        """Este método é fornecido
        
        1. Libere o controle do drone
        2. Pare a conexão (e o log de telemetria)
        3. Encerre a missão
        4. Transição para o estado MANUAL
        """
        print("transição manual")

        self.liberar_controle()
        self.parar()
        self.em_missao = False
        self.estado_voo = Estados.MANUAL

    def iniciar(self):
        """Este método é fornecido
        
        1. Abra um arquivo de log
        2. Inicie a conexão do drone
        3. Feche o arquivo de log
        """
        print("Criando arquivo de log")
        self.iniciar_log("Logs", "NavLog.txt")
        print("iniciando conexão")
        self.conexao.start()
        print("Fechando arquivo de log")
        self.stop_log()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--porta', type=int, default=5760, help='Número da porta')
    parser.add_argument('--host', type=str, default='127.0.0.1', help="endereço do host, ou seja, '127.0.0.1'")
    args = parser.parse_args()

    conn = MavlinkConnection('tcp:{0}:{1}'.format(args.host, args.porta), threaded=False, PX4=False)
    #conn = WebSocketConnection('ws://{0}:{1}'.format(args.host, args.porta))
    drone = BackyardFlyer(conn)
    time.sleep(2)
    drone.iniciar()
import argparse
import time
from enum import Enum

import numpy as np

from udacidrone import Drone
from udacidrone.connection import MavlinkConnection, WebSocketConnection  # noqa: F401
from udacidrone.messaging import MsgID


class Estados(Enum):
    MANUAL = 0
    ARMAMENTO = 1
    DECOLAGEM = 2
    WAYPOINT = 3
    POUSO = 4
    DESARMAMENTO = 5


class BackyardFlyer(Drone):

    def __init__(self, connection):
        super().__init__(connection)
        self.posicao_alvo = np.array([0.0, 0.0, 0.0])
        self.todos_waypoints = []
        self.em_missao = True
        self.verificar_estado = {}

        # estado inicial
        self.estado_voo = Estados.MANUAL

        # TODO: Registre todos os seus callbacks aqui
        self.registrar_callback(MsgID.LOCAL_POSITION, self.callback_posicao_local)
        self.registrar_callback(MsgID.LOCAL_VELOCITY, self.callback_velocidade_local)
        self.registrar_callback(MsgID.STATE, self.callback_estado)

    def callback_posicao_local(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.LOCAL_POSITION` é recebido e self.local_position contém novos dados
        """
        pass

    def callback_velocidade_local(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.LOCAL_VELOCITY` é recebido e self.local_velocity contém novos dados
        """
        pass

    def callback_estado(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.STATE` é recebido e self.armed e self.guided contêm novos dados
        """
        pass

    def calcular_quadrado(self):
        """TODO: Preencha este método
        
        1. Retorna waypoints para voar em um quadrado
        """
        pass

    def transicao_armamento(self):
        """TODO: Preencha este método
        
        1. Assuma o controle do drone
        2. Passe um comando de armamento
        3. Defina a localização inicial como a posição atual
        4. Transição para o estado ARMAMENTO
        """
        print("transição de armamento")

    def transicao_decolagem(self):
        """TODO: Preencha este método
        
        1. Defina a altitude da posição alvo como 3.0m
        2. Comande uma decolagem para 3.0m
        3. Transição para o estado DECOLAGEM
        """
        print("transição de decolagem")

    def transicao_waypoint(self):
        """TODO: Preencha este método
    
        1. Comande a próxima posição de waypoint
        2. Transição para o estado WAYPOINT
        """
        print("transição de waypoint")

    def transicao_pouso(self):
        """TODO: Preencha este método
        
        1. Comande o drone para pousar
        2. Transição para o estado POUSO
        """
        print("transição de pouso")

    def transicao_desarmamento(self):
        """TODO: Preencha este método
        
        1. Comande o drone para desarmar
        2. Transição para o estado DESARMAMENTO
        """
        print("transição de desarmamento")

    def transicao_manual(self):
        """Este método é fornecido
        
        1. Libere o controle do drone
        2. Pare a conexão (e o log de telemetria)
        3. Encerre a missão
        4. Transição para o estado MANUAL
        """
        print("transição manual")

        self.liberar_controle()
        self.parar()
        self.em_missao = False
        self.estado_voo = Estados.MANUAL

    def iniciar(self):
        """Este método é fornecido
        
        1. Abra um arquivo de log
        2. Inicie a conexão do drone
        3. Feche o arquivo de log
        """
        print("Criando arquivo de log")
        self.iniciar_log("Logs", "NavLog.txt")
        print("iniciando conexão")
        self.conexao.start()
        print("Fechando arquivo de log")
        self.parar_log()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--porta', type=int, default=5760, help='Número da porta')
    parser.add_argument('--host', type=str, default='127.0.0.1', help="endereço do host, ou seja, '127.0.0.1'")
    args = parser.parse_args()

    conn = MavlinkConnection('tcp:{0}:{1}'.format(args.host, args.porta), threaded=False, PX4=False)
    #conn = WebSocketConnection('ws://{0}:{1}'.format(args.host, args.porta))
    drone = BackyardFlyer(conn)
    time.sleep(2)
    drone.iniciar()import argparse
import time
from enum import Enum

import numpy as np

from udacidrone import Drone
from udacidrone.connection import MavlinkConnection, WebSocketConnection  # noqa: F401
from udacidrone.messaging import MsgID


class Estados(Enum):
    MANUAL = 0
    ARMAMENTO = 1
    DECOLAGEM = 2
    WAYPOINT = 3
    POUSO = 4
    DESARMAMENTO = 5


class BackyardFlyer(Drone):

    def __init__(self, connection):
        super().__init__(connection)
        self.posicao_alvo = np.array([0.0, 0.0, 0.0])
        self.todos_waypoints = []
        self.em_missao = True
        self.verificar_estado = {}

        # estado inicial
        self.estado_voo = Estados.MANUAL

        # TODO: Registre todos os seus callbacks aqui
        self.registrar_callback(MsgID.LOCAL_POSITION, self.callback_posicao_local)
        self.registrar_callback(MsgID.LOCAL_VELOCITY, self.callback_velocidade_local)
        self.registrar_callback(MsgID.STATE, self.callback_estado)

    def callback_posicao_local(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.LOCAL_POSITION` é recebido e self.local_position contém novos dados
        """
        pass

    def callback_velocidade_local(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.LOCAL_VELOCITY` é recebido e self.local_velocity contém novos dados
        """
        pass

    def callback_estado(self):
        """
        TODO: Implemente este método

        Isso é acionado quando `MsgID.STATE` é recebido e self.armed e self.guided contêm novos dados
        """
        pass

    def calcular_quadrado(self):
        """TODO: Preencha este método
        
        1. Retorna waypoints para voar em um quadrado
        """
        pass

    def transicao_armamento(self):
        """TODO: Preencha este método
        
        1. Assuma o controle do drone
        2. Passe um comando de armamento
        3. Defina a localização inicial como a posição atual
        4. Transição para o estado ARMAMENTO
        """
        print("transição de armamento")

    def transicao_decolagem(self):
        """TODO: Preencha este método
        
        1. Defina a altitude da posição alvo como 3.0m
        2. Comande uma decolagem para 3.0m
        3. Transição para o estado DECOLAGEM
        """
        print("transição de decolagem")

    def transicao_waypoint(self):
        """TODO: Preencha este método
    
        1. Comande a próxima posição de waypoint
        2. Transição para o estado WAYPOINT
        """
        print("transição de waypoint")

    def transicao_pouso(self):
        """TODO: Preencha este método
        
        1. Comande o drone para pousar
        2. Transição para o estado POUSO
        """
        print("transição de pouso")

    def transicao_desarmamento(self):
        """TODO: Preencha este método
        
        1. Comande o drone para desarmar
        2. Transição para o estado DESARMAMENTO
        """
        print("transição de desarmamento")

    def transicao_manual(self):
        """Este método é fornecido
        
        1. Libere o controle do drone
...         2. Pare a conexão (e o log de telemetria)
...         3. Encerre a missão
...         4. Transição para o estado MANUAL
...         """
...         print("transição manual")
... 
...         self.liberar_controle()
...         self.parar()
...         self.em_missao = False
...         self.estado_voo = Estados.MANUAL
... 
...     def iniciar(self):
...         """Este método é fornecido
...         
...         1. Abra um arquivo de log
...         2. Inicie a conexão do drone
...         3. Feche o arquivo de log
...         """
...         print("Criando arquivo de log")
...         self.iniciar_log("Logs", "NavLog.txt")
...         print("iniciando conexão")
...         self.conexao.start()
...         print("Fechando arquivo de log")
...         self.parar_log()
... 
... 
... if __name__ == "__main__":
...     parser = argparse.ArgumentParser()
...     parser.add_argument('--porta', type=int, default=5760, help='Número da porta')
...     parser.add_argument('--host', type=str, default='127.0.0.1', help="endereço do host, ou seja, '127.0.0.1'")
...     args = parser.parse_args()
... 
...     conn = MavlinkConnection('tcp:{0}:{1}'.format(args.host, args.porta), threaded=False, PX4=False)
...     #conn = WebSocketConnection('ws://{0}:{1}'.format(args.host, args.porta))
...     drone = BackyardFlyer(conn)
...     time.sleep(2)
