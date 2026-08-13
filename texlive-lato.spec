%global tl_name lato
%global tl_revision 79618
%global tl_version 3.3

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Lato font family and LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/lato
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Lato is a sanserif typeface family designed in the Summer 2010 by
Warsaw-based designer Lukasz Dziedzic for the tyPoland foundry. This
font, which includes five weights (hairline, light, regular, bold and
black), is available from the Google Font Directory as TrueType files
under the Open Font License version 1.1. The package provides support
for this font in LaTeX. It includes the original TrueType fonts, as well
as Type 1 versions, converted for this package using FontForge for full
support with Dvips.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from lato:
Map lato.map
TL_DROPIN_EOF
