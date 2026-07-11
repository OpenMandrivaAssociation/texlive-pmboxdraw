%global tl_name pmboxdraw
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Poor mans box drawing characters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pmboxdraw
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pmboxdraw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pmboxdraw.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pmboxdraw.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package declares box drawing characters of old code pages, e.g.
cp437. It uses rules instead of using a font.

