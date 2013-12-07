# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/stdclsdv
# catalog-date 2009-09-04 12:14:45 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-stdclsdv
Version:	1.1a
Release:	4
Summary:	Provide sectioning information for package writers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stdclsdv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stdclsdv.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-2
+ Revision: 756244
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 719585
- texlive-stdclsdv
- texlive-stdclsdv
- texlive-stdclsdv
- texlive-stdclsdv

