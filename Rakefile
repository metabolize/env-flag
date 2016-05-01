$mac_os = `uname -s`.strip == 'Darwin'

desc "Install dependencies for distribution"
task :install_dist do
    if $mac_os
        raise unless system "brew update"
        raise unless system "brew install pandoc"
    else
        puts
        puts "You must install:"
        puts
        puts " - pandoc"
        puts
        raise
    end
end

def command_is_in_path?(command)
    system("which #{ command} > /dev/null 2>&1")
end

task :test do
  raise unless system "nose2"
end

task :lint do
  raise unless system "./pylint_test.py baiji --min_rating 10.0"
end

task :test_for_ci => [
    :test,
    :lint,
]

desc "Remove .pyc files"
task :clean do
    system "find . -name '*.pyc' -delete"
end

task :sdist do
    unless command_is_in_path? 'pandoc'
        puts
        puts "Please install pandoc."
        puts
        raise
    end
    raise unless system "python setup.py sdist"
end

task :upload do
    unless command_is_in_path?('pandoc')
        puts
        puts "Please install pandoc."
        puts
        raise
    end
    raise unless system "python setup.py sdist upload"
end
