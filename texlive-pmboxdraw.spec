Name:		texlive-pmboxdraw
Version:	53046
Release:	2
Summary:	Poor man's box drawing characters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pmboxdraw
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmboxdraw.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmboxdraw.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmboxdraw.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package declares box drawing characters of old code pages,
e.g. cp437. It uses rules instead of using a font.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pmboxdraw
%{_texmfdistdir}/tex/latex/pmboxdraw
%doc %{_texmfdistdir}/doc/latex/pmboxdraw

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
