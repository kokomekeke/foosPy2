import multiprocessing
import sys
from asyncio import wait
from concurrent.futures import ProcessPoolExecutor
from signal import signal, SIGINT, SIGTERM

from loop import Loop


class CommAggregate(Loop):
    """Background process for managing the connections and communications to the UAVs"""

    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        self._telemetry_to_monitoring = None
        self.i = 1
        # Loop.__init__(self, *args, **kwargs)
        print("__init__")
        super().__init__(*args, **kwargs)

    def __call__(
        self,
        telemetry_to_monitoring,
        *args,
        **kwargs,
    ) -> None:
        print("__call__")
        self._telemetry_to_monitoring = telemetry_to_monitoring
        return super()._call(*args, **kwargs)

    def _recv_thread(self) -> None:
        pass

    def _receive_telemetry(
        self, uav_entity, packet
    ) -> None:
        print("telemetry")

    def _receive_measurement(
        self, uav_entity, packet
    ) -> None:
        print("receieve measurement")

    def _receive_event(self, uav_entity, packet) -> None:
       print("receive event")

    def _receive_operror(
        self, uav_entity, packet
    ) -> None:
        print("receive operror")

    def _receive_packet(
        self
    ) -> None:
        # print("packet")
        pass

    def _loop(self) -> None:
        if self.i == 1:
            print("cloop")
        self._receive_packet()
        self.i += 1
        pass


class Commander:
    def __init__(
        self,
    ) -> None:

        self._manager = multiprocessing.Manager()
        self._telemetry_for_monitoring_q = self._manager.Queue(maxsize=8)
        self._pool = ProcessPoolExecutor(max_workers=14)

        self._commaggregate = CommAggregate()

    def start(self) -> None:
        """Start all background processes"""

        commaggregate_future = self._pool.submit(
            self._commaggregate, self._telemetry_for_monitoring_q
        )

        signal(SIGINT, self._signal_handler)
        signal(SIGTERM, self._signal_handler)
        # while True:
        #     done, running = wait(
        #         (
        #             commaggregate_future,
        #         ),
        #         timeout=1,
        #     )
        #     if self._pool._max_workers < len(running):
        #         print("aa")
        #         return
        #     for future in done:
        #         if future.exception(0) is not None:
        #             print("bb")
        #             return

    def _signal_handler(self, signal, frame) -> None:
        self._pool.shutdown()
        self._manager.shutdown()
        sys.exit(0)

if "__main__" == __name__:
    cmd = Commander()
    cmd.start()