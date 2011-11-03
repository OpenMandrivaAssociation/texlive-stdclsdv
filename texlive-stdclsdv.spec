# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/stdclsdv
# catalog-date 2009-09-04 12:14:45 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-stdclsdv
Version:	1.1a
Release:	1
Summary:	Provide sectioning information for package writers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stdclsdv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The stdclsdv package is designed for package writers who need
to know what sectioning divsions are provided by the document's
class. It also provides a version of \CheckCommand that sets a
flag rather than printing a warning.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
