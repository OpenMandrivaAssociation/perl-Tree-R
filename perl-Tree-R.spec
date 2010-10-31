%define		pdir	Tree
%define		pnam	R
Summary:	Tree::R - Perl extension for the Rtree data structure and algorithms
Name:		perl-Tree-R
Version:	0.06
Release:	%mkrel 1
License:	GPL
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AJ/AJOLMA/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://cpansearch.perl.org/src/AJOLMA/
BuildRequires:	perl-devel >= 1:5.8.0

%description
Tree::R - Perl extension for the Rtree data structure and algorithms


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%__perl Makefile.PL \
     INSTALLDIRS=

%make


%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%files
%defattr(-,root,root) 
%doc Changes README
%{perl_sitelib}/Tree/R.pm
%{perl_sitelib}/auto/Tree/R/autosplit.ix
%{_usr}/local/share/man/man3/Tree::R.3pm




