%define name rexgrep
%define version 1.2
%define release  %mkrel ease

Summary:   A graphical frontend to the grep command
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source0:   %{name}-%{version}.tar.bz2
Requires:	xterm
Requires:	man
Buildrequires:	gtk+1.2-devel
Buildrequires:	xterm
Buildrequires:	man
BuildRoot: %{_tmppath}/%{name}-root
Prefix:    %{_prefix}
License: GPL
Group:     File tools
URL:	   http://rexgrep.tripod.com/rexgrep.htm

%description
Rexgrep is a graphical frontend to the grep command.
Rexgrep combines the power of the 'grep' command with the convenience of 
a very easy to use graphical user interface, while not compromising on its
functionality.

%prep
  [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
  && rm -rf ${RPM_BUILD_ROOT}

%setup

%configure

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall

(mkdir -p ${RPM_BUILD_ROOT}%{_menudir}
cat > ${RPM_BUILD_ROOT}%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{name}"\
title="ReXgrep"\
longtitle="%{summary}"\
needs="x11"\
icon="file_tools_section.png"\
section="Applications/File tools"
EOF
)

%post
%update_menus
 
%postun
%clean_menus  

%clean
  [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
  && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/rexgrep
%{_mandir}/man1/rexgrep.1*
%{_menudir}/%{name}

