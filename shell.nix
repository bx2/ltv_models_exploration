with import <nixpkgs> {};
let
  my-python-packages = python-packages: [
    python-packages.setuptools
    python-packages.wheel
    python-packages.pip
  ];
  my-python = python311.withPackages my-python-packages;
in
  pkgs.mkShell {
    buildInputs = [
      my-python
    ];
    shellHook = ''
      export PIP_PREFIX="$(pwd)/__pypackages__/"
      export PATH="$(pwd)/__pypackages__/bin:$PATH"
      export PYTHONPATH="$(pwd)/__pypackages__/lib/python3.11/site-packages:$(pwd)/src"
      export PYTHONBREAKPOINT=ipdb.set_trace
      unset SOURCE_DATE_EPOCH
      pip install -r "$(pwd)/requirements.txt"
      source .env
    '';
  }
