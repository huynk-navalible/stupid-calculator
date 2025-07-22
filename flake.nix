{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let 
  	pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in {

    packages.x86_64-linux.python3 = nixpkgs.legacyPackages.x86_64-linux.python3;

    packages.x86_64-linux.default = self.packages.x86_64-linux.python3;


    # the shell 
    devShells.x86_64-linux.default = pkgs.mkShell {
    	buildInputs = with pkgs; [
		python3Full
		tk
		git
		curl
		fastfetch
		pipx
		gcc
		micro
	];

	shellHook = ''
		echo "shell is ready fuck u"
	'';
    }; 

  };
}
