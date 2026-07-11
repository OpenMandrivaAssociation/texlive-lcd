%global tl_name lcd
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Alphanumerical LCD-style displays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lcd
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lcd.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package that will display text as on an (early) LCD display (the
output is very visibly pixellated). Assumes 8-bit input in its internal
verbatim-style environment.

