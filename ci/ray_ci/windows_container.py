import subprocess
import sys
from typing import List, Optional

from ci.ray_ci.container import Container


class WindowsContainer(Container):
    def install_ray(self, build_type: Optional[str] = None) -> List[str]:
        subprocess.check_call(
            [
                "docker",
                "build",
                "-t",
                self._get_docker_image(),
                "-f",
                "c:\\workdir\\ci\\ray_ci\\tests.windows.env.Dockerfile",
                "c:\\workdir",
            ],
            stdout=sys.stdout,
            stderr=sys.stderr,
        )

    def _get_run_command(
        self,
        script: List[str],
        gpu_ids: Optional[List[int]] = None,
    ) -> List[str]:
        return [
            "docker",
            "run",
            "-i",
            "--rm",
            self._get_docker_image(),
            "bash",
            "-c",
            "\n".join(script),
        ]
