# revision 24489
# category Package
# catalog-ctan /fonts/lato
# catalog-date 2011-11-03 09:19:42 +0100
# catalog-license lppl1.3
# catalog-version 2.1
Name:		texlive-lato
Version:	2.1
Release:	2
Summary:	Lato font fanily and LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/lato
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lato.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Black-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Black.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-BlackItalic-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-BlackItalic.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Bold-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Bold.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-BoldItalic-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Hairline-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Hairline.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-HairlineItalic-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-HairlineItalic.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Italic-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Italic.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Light-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Light.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-LightItalic-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-LightItalic.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Regular-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/lato/lato-01.enc
%{_texmfdistdir}/fonts/enc/dvips/lato/lato-02.enc
%{_texmfdistdir}/fonts/enc/dvips/lato/lato-dotlessj.enc
%{_texmfdistdir}/fonts/map/dvips/lato/lato.map
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Black-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Black-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Black-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Black-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Black-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Black-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Black-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Black-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlackItalic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlackItalic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlackItalic-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlackItalic-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlackItalic-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlackItalic-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlackItalic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlackItalic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bold-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bold-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bold-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bold-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bold-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bold-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bold-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bold-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BoldItalic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BoldItalic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BoldItalic-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BoldItalic-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BoldItalic-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BoldItalic-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BoldItalic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BoldItalic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hairline-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hairline-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hairline-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hairline-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hairline-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hairline-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hairline-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hairline-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HairlineItalic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HairlineItalic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HairlineItalic-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HairlineItalic-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HairlineItalic-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HairlineItalic-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HairlineItalic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HairlineItalic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Italic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Italic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Italic-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Italic-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Italic-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Italic-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Italic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Italic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Light-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Light-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Light-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Light-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Light-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Light-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Light-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Light-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LightItalic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LightItalic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LightItalic-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LightItalic-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LightItalic-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LightItalic-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LightItalic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LightItalic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Regular-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Regular-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Regular-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Regular-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Regular-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Regular-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Regular-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Regular-ts1.tfm
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Black.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-BlackItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Hairline.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-HairlineItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Italic.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Light.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-LightItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Regular.ttf
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Black-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Black.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-BlackItalic-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-BlackItalic.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Bold-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-BoldItalic-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Hairline-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Hairline.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-HairlineItalic-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-HairlineItalic.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Italic-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Light-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Light.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-LightItalic-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-LightItalic.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Regular-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Black-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Black-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Black-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Black-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Black-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlackItalic-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlackItalic-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlackItalic-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlackItalic-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlackItalic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bold-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bold-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bold-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bold-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bold-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BoldItalic-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BoldItalic-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BoldItalic-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BoldItalic-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BoldItalic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hairline-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hairline-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hairline-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hairline-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hairline-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HairlineItalic-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HairlineItalic-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HairlineItalic-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HairlineItalic-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HairlineItalic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Italic-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Italic-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Italic-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Italic-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Italic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Light-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Light-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Light-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Light-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Light-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LightItalic-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LightItalic-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LightItalic-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LightItalic-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LightItalic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Regular-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Regular-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Regular-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Regular-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Regular-ts1.vf
%{_texmfdistdir}/tex/latex/lato/lato.sty
%{_texmfdistdir}/tex/latex/lato/ot1fla.fd
%{_texmfdistdir}/tex/latex/lato/t1fla.fd
%{_texmfdistdir}/tex/latex/lato/ts1fla.fd
%doc %{_texmfdistdir}/doc/fonts/lato/CHANGES
%doc %{_texmfdistdir}/doc/fonts/lato/README
%doc %{_texmfdistdir}/doc/fonts/lato/lato-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/lato/lato-samples.tex
%doc %{_texmfdistdir}/doc/fonts/lato/lato.pdf
%doc %{_texmfdistdir}/doc/fonts/lato/lato.tex
%doc %{_texmfdistdir}/doc/fonts/lato/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/lato/Makefile
%doc %{_texmfdistdir}/source/fonts/lato/lato-01.etx
%doc %{_texmfdistdir}/source/fonts/lato/lato-02.etx
%doc %{_texmfdistdir}/source/fonts/lato/lato-dotlessj.etx
%doc %{_texmfdistdir}/source/fonts/lato/lato-drv.tex
%doc %{_texmfdistdir}/source/fonts/lato/lato-fixlatin.mtx
%doc %{_texmfdistdir}/source/fonts/lato/lato-fixtextcomp.mtx
%doc %{_texmfdistdir}/source/fonts/lato/lato-map.tex
%doc %{_texmfdistdir}/source/fonts/lato/ttf2type1.pe

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
