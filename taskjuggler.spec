#
# Conditional build:
%bcond_with	pch		# enable precompiled headers
#
Summary:	TaskJuggler - a project management tool
Name:		taskjuggler
Version:	2.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.taskjuggler.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	a4d77f4c8f7a453fd230d550dd4d2180
Source1:	http://www.taskjuggler.org/download/manual-%{version}.tar.bz2
# Source1-md5:	15c2d3d9eeba04f7f4c72090424be300
URL:		http://www.taskjuggler.org/
%if %{with_pch}
BuildRequires:	gcc >= 3.4
BuildRequires:	unsermake
%endif
BuildRequires:	jadetex
BuildRequires:	kdelibs-devel >= 3.3
BuildRequires:	libxslt-devel
BuildRequires:	openjade
BuildRequires:	perl-base
#BuildRequires:	tetex*
#BuildRequires:	Perl module Date::Calc... not found
#BuildRequires:	Perl module XML::Parser... not found
#BuildRequires:	Perl module Class::MethodMaker... not found
#BuildRequires:	Perl module PostScript::Simple... not found
#BuildRequires:	poster... no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Taskjuggler is a project management tool for Linux and UNIX
system-based operating systems. Whether you want to plan your
colleague's shifts for the next month or want to build a skyscraper -
Taskjuggler is the tool for you. Instead of clicking yourself
painfully through hundreds of dialog boxes you specify your
Taskjuggler project in a simple text format. You simply list all your
tasks and their dependencies. The information is sent through
Taskjuggler and you will get all sorts of reports in HTML or XML
format. Taskjuggler does not only honor the task interdependencies but
also takes resource constrains into account. Using Taskjuggler's
powerful filtering and reporting algorithms you can create task lists,
resource usage tables, status reports, project calendars and project
accounting statements.

%prep
%setup -q -a1

%build
#{__libtoolize}
#{__aclocal}
#{__autoconf}
#{__autoheader}
#{__automake}
%configure \
	%{?with_pch:--enable-pch} \
	--disable-final \
	--with-kde-support=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
#config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
#attr(755,root,root) %{_bindir}/*
#{_datadir}/%{name}

# initscript and its config
#attr(754,root,root) /etc/rc.d/init.d/%{name}
#config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

#files subpackage
#defattr(644,root,root,755)
#doc extras/*.gz
#{_datadir}/%{name}-ext
