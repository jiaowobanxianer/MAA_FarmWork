import sys

from maa.agent.agent_server import AgentServer
from maa.custom_recognition import CustomRecognition
from maa.custom_action import CustomAction
from maa.toolkit import Toolkit
import my_action
import my_reco


def main():
    Toolkit.init_option("./")

    socket_id = sys.argv[-1]

    AgentServer.start_up(socket_id)
    AgentServer.join()
    AgentServer.shut_down()

if __name__ == "__main__":
    main()
