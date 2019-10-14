__all__ = ("TargetTriple", "pythonTriple")
import sys
import typing


class TargetTripleParser:
	__slots__ = ("archs", "oses", "abis")

	def __init__(self, archs: typing.Set[str], oses: typing.Set[str], abis: typing.Set[str]):
		self.archs = archs
		self.oses = oses
		self.abis = abis


class _TargetTriple:
	__slots__ = ("arch", "bitness", "os", "abi")

	def __init__(self, arch: typing.Optional[str] = None, os: typing.Optional[str] = None, abi: typing.Optional[str] = None, bitness: typing.Optional[int] = None) -> None:
		self.arch = arch
		self.os = os
		self.abi = abi
		self.bitness = bitness

	@classmethod
	def parse(cls, s: str, parser: TargetTripleParser) -> "_TargetTriple":

		return cls()

	def getTuple(self) -> typing.Tuple[str, str, str]:
		return (self.arch, self.os, self.abi)

	def __str__(self) -> str:
		return "-".join(self.getTuple())

	def __repr__(self) -> str:
		return self.__class__.__name__ + "(" + ", ".join(repr(c) for c in self.getTuple()) + ")"

	def __hash__(self) -> int:
		return hash(self.getTuple())

	def __eq__(self, other: "_TargetTriple") -> bool:
		if isinstance(other, str):
			return other == str(self)
		else:
			return self.getTuple() == other.getTuple()


pythonTriple = sys.implementation._multiarch.split("-")
pythonTriple = _TargetTriple(pythonTriple[0], pythonTriple[1], pythonTriple[2])


class TargetTriple(_TargetTriple):
	__slots__ = ()

	def __init__(self, arch: typing.Optional[str] = None, os: typing.Optional[str] = None, abi: typing.Optional[str] = None, bitness: typing.Optional[int] = None) -> None:
		arch = arch if arch is not None else pythonTriple.arch
		os = os if os is not None else pythonTriple.os
		abi = abi if abi is not None else pythonTriple.abi
		bitness = bitness if bitness is not None else pythonTriple.bitness
		super().__init__(arch, os, abi, bitness)
