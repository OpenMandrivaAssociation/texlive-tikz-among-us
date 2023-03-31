Name:		texlive-tikz-among-us
Version:	60880
Release:	2
Summary:	Create some AmongUs characters in TikZ environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-among-us
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-among-us.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-among-us.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package recreates some AmongUs characters in TikZ
environments. Some interesting uses alongside other packages
are also supported.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-among-us
%doc %{_texmfdistdir}/doc/latex/tikz-among-us

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
