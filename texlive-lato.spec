%global tl_name lato
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.3
Release:	%{tl_revision}.1
Summary:	Lato font family and LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/lato
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Lato is a sanserif typeface family designed in the Summer 2010 by
Warsaw-based designer Lukasz Dziedzic for the tyPoland foundry. This
font, which includes five weights (hairline, light, regular, bold and
black), is available from the Google Font Directory as TrueType files
under the Open Font License version 1.1. The package provides support
for this font in LaTeX. It includes the original TrueType fonts, as well
as Type 1 versions, converted for this package using FontForge for full
support with Dvips.

