Name: sdl2-c++11
Version: 1
Release: alt1
Summary: Example SDL2 to c++11
Group: Graphics

License: BSD-3-Clause
Url: https://github.com/xyproto/sdl2-examples
Source0: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libSDL2-devel

%description
This example of package SDL2 c++11.

URL resources:
https://alt-packaging-guide.github.io/
https://www.altlinux.org/Hasher/FAQ

# распаковка архива из Source0
%prep
%setup

# команда для фактической сборки программного обеспечения
# в машинный код (исполняемый файл)
%build
%make_build

# создаются две директории %_bindir и %_datadir/%name в
# %buildroot (который во время сборки пакета эмулирует конечные
# пути установки файлов в систему)
# копирование исполняемого файла в раздел %_bindir
# копирование изображения в раздел %_datadir/%name
%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name
install -Dm 755 main %buildroot%_bindir/%name
install -Dm 644 grumpy-cat.bmp -t %buildroot%_datadir/%name

# список файлов, которые будут установлены в системе конечного
# пользователя
%files
%dir %_datadir/%name
%_bindir/%name
%_datadir/%name/grumpy-cat.bmp

# запись изменений, произошедших с пакетом между различными
# Version или Release сборками
%changelog
* Tue Apr 22 2025 Artem Stefanski <gargulia@altlinux.org> 1-alt1
- Initial build.
