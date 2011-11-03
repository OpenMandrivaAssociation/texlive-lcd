# revision 16549
# category Package
# catalog-ctan /macros/latex/contrib/lcd
# catalog-date 2006-11-14 20:05:17 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-lcd
Version:	0.3
Release:	1
Summary:	Alphanumerical LCD-style displays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lcd
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A LaTeX package that will display text as on an LCD display.
Assumes 8-bit input in its internal verbatim-style environment.

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
%{_texmfdistdir}/tex/latex/lcd/lcd.sty
%doc %{_texmfdistdir}/doc/latex/lcd/00readme
%doc %{_texmfdistdir}/doc/latex/lcd/example.pdf
%doc %{_texmfdistdir}/doc/latex/lcd/example.tex
#- source
%doc %{_texmfdistdir}/source/latex/lcd/lcd.dtx
%doc %{_texmfdistdir}/source/latex/lcd/lcd.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
