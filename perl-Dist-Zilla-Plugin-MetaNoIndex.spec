%define upstream_name    Dist-Zilla-Plugin-MetaNoIndex
Name:		perl-%{upstream_name}
Version:	1.101550
Release:	6

Summary:	Stop CPAN from indexing stuff
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Data::PowerSet)
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Modern::Perl)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Readonly)

BuildArch:	noarch

%description
This plugin allows you to prevent PAUSE/CPAN from indexing files you don't
want indexed. This is useful if you build test classes or example classes
that are used for those purposes only, and are not part of the
distribution. It does this by adding a 'no_index' block to your _META.yml_
file in your distribution.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

