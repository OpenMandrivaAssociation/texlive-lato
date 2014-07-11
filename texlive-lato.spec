# revision 24986
# category Package
# catalog-ctan /fonts/lato
# catalog-date 2011-12-31 13:07:31 +0100
# catalog-license lppl1.3
# catalog-version 2.2
Name:		texlive-lato
Version:	2.2
Release:	7
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
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Bla-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Bla.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-BlaIta-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-BlaIta.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Bol-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Bol.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-BolIta-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-BolIta.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Hai-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Hai.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-HaiIta-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-HaiIta.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Lig-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Lig.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-LigIta-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-LigIta.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Reg-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-Reg.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-RegIta-LCDFJ.afm
%{_texmfdistdir}/fonts/afm/public/lato/Lato-RegIta.afm
%{_texmfdistdir}/fonts/enc/dvips/lato/lato-01.enc
%{_texmfdistdir}/fonts/enc/dvips/lato/lato-02.enc
%{_texmfdistdir}/fonts/enc/dvips/lato/lato-dotlessj.enc
%{_texmfdistdir}/fonts/map/dvips/lato/lato.map
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bla-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bla-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bla-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bla-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bla-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bla-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bla-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bla-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlaIta-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlaIta-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlaIta-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlaIta-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlaIta-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlaIta-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlaIta-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BlaIta-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bol-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bol-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bol-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bol-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bol-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bol-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bol-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Bol-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BolIta-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BolIta-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BolIta-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BolIta-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BolIta-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BolIta-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BolIta-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-BolIta-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hai-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hai-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hai-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hai-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hai-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hai-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hai-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Hai-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HaiIta-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HaiIta-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HaiIta-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HaiIta-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HaiIta-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HaiIta-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HaiIta-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-HaiIta-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Lig-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Lig-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Lig-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Lig-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Lig-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Lig-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Lig-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Lig-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LigIta-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LigIta-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LigIta-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LigIta-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LigIta-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LigIta-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LigIta-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-LigIta-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Reg-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Reg-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Reg-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Reg-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Reg-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Reg-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Reg-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-Reg-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-RegIta-01.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-RegIta-02.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-RegIta-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-RegIta-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-RegIta-dotlessj.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-RegIta-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-RegIta-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/lato/Lato-RegIta-ts1.tfm
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Bla.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-BlaIta.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Bol.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-BolIta.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Hai.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-HaiIta.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Lig.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-LigIta.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-Reg.ttf
%{_texmfdistdir}/fonts/truetype/public/lato/Lato-RegIta.ttf
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Bla-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Bla.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-BlaIta-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-BlaIta.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Bol-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Bol.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-BolIta-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-BolIta.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Hai-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Hai.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-HaiIta-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-HaiIta.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Lig-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Lig.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-LigIta-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-LigIta.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Reg-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-Reg.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-RegIta-LCDFJ.pfb
%{_texmfdistdir}/fonts/type1/public/lato/Lato-RegIta.pfb
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bla-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bla-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bla-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bla-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bla-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlaIta-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlaIta-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlaIta-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlaIta-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BlaIta-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bol-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bol-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bol-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bol-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Bol-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BolIta-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BolIta-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BolIta-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BolIta-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-BolIta-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hai-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hai-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hai-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hai-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Hai-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HaiIta-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HaiIta-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HaiIta-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HaiIta-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-HaiIta-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Lig-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Lig-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Lig-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Lig-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Lig-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LigIta-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LigIta-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LigIta-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LigIta-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-LigIta-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Reg-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Reg-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Reg-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Reg-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-Reg-ts1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-RegIta-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-RegIta-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-RegIta-ot1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-RegIta-t1.vf
%{_texmfdistdir}/fonts/vf/public/lato/Lato-RegIta-ts1.vf
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


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 758934
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 753205
- Rebuild to reduce used resources

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 729675
- texlive-lato

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 718832
- texlive-lato
- texlive-lato
- texlive-lato
- texlive-lato

