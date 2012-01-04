# revision 16549
# category Package
# catalog-ctan /macros/latex/contrib/lcd
# catalog-date 2006-11-14 20:05:17 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-lcd
Version:	0.3
Release:	2
Summary:	Alphanumerical LCD-style displays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lcd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package that will display text as on an LCD display.
Assumes 8-bit input in its internal verbatim-style environment.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lcd/lcd.sty
%doc %{_texmfdistdir}/doc/latex/lcd/00readme
%doc %{_texmfdistdir}/doc/latex/lcd/example.pdf
%doc %{_texmfdistdir}/doc/latex/lcd/example.tex
#- source
%doc %{_texmfdistdir}/source/latex/lcd/lcd.dtx
%doc %{_texmfdistdir}/source/latex/lcd/lcd.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
