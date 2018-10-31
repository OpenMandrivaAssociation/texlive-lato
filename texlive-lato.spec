Name:		texlive-lato
Version:	3.0
Release:	2
Summary:	Lato font fanily and LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/lato
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Lato is a sanserif typeface family designed in the Summer 2010
by Warsaw-based designer Lukasz Dziedzic for the tyPoland
foundry. This font, which includes five weights (hairline,
light, regular, bold and black), is available from the Google
Font Directory as TrueType files under the Open Font License
version 1.1. The package provides support for this font in
LaTeX. It includes the original TrueType fonts, as well as Type
1 versions, converted for this package using FontForge for full
support with Dvips.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/lato
%{_texmfdistdir}/fonts/map/dvips/lato
%{_texmfdistdir}/fonts/tfm/typoland/lato
%{_texmfdistdir}/fonts/truetype/typoland/lato
%{_texmfdistdir}/fonts/type1/typoland/lato
%{_texmfdistdir}/fonts/vf/typoland/lato
%{_texmfdistdir}/tex/latex/lato
%doc %{_texmfdistdir}/doc/fonts/lato

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
