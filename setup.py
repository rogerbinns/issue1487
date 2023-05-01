import sys

from setuptools import setup, Extension
from distutils.command import build


class custom_build(build.build):
    user_options = (build.build.user_options +
                    [("marker-sentinel", None, "marker for the issue")])

    def initialize_options(self):
        self.marker_sentinel = None
        return super().initialize_options()

    def finalize_options(self):
        print(f"ISSUE 1487: marker serntinel is { self.marker_sentinel }",
              file=sys.stderr)
        return super().finalize_options()


setup(name="custom",
      version="1.0",
      ext_modules=[Extension("custom", ["src/custom.c"])],
      cmdclass={"build": custom_build})
