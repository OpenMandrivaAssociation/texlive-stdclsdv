%global tl_name stdclsdv
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Provide sectioning information for package writers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stdclsdv
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The stdclsdv package is designed for package writers who need to know
what sectioning divisions are provided by the document's class. It also
provides a version of \CheckCommand that sets a flag rather than
printing a warning.

