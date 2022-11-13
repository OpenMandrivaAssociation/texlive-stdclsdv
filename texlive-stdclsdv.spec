Name:		texlive-stdclsdv
Version:	15878
Release:	1
Summary:	Provide sectioning information for package writers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stdclsdv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The stdclsdv package is designed for package writers who need
to know what sectioning divsions are provided by the document's
class. It also provides a version of \CheckCommand that sets a
flag rather than printing a warning.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stdclsdv/stdclsdv.sty
%doc %{_texmfdistdir}/doc/latex/stdclsdv/README
%doc %{_texmfdistdir}/doc/latex/stdclsdv/stdclsdv.pdf
#- source
%doc %{_texmfdistdir}/source/latex/stdclsdv/stdclsdv.dtx
%doc %{_texmfdistdir}/source/latex/stdclsdv/stdclsdv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
