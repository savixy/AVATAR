clear
clc

trajectory = zeros(200, 6);

J1 = (linspace(0, 0.538, 250))';
J2 = (linspace(0, 0.7637362481385295, 250))';
J3 = (linspace(-1.57, -1.8800761286392603, 250))';
J4 = (linspace(0, -0.10164862748520956, 250))';
J5 = (linspace(1.57, 0.4487, 250))';
J6 = (linspace(0, 0.5795, 250))';

for i = 1:size(J1)
    trajectory(i, 1) = J1(i);
    trajectory(i, 2) = J2(i);
    trajectory(i, 3) = J3(i);
    trajectory(i, 4) = J4(i);
    trajectory(i, 5) = J5(i);
    trajectory(i, 6) = J6(i);
end

file = fopen('C:\Users\Aca\Desktop\AVATAR 2023\TRAJECTORY_0.txt', 'w');
j1 = '        "J1": %.15f,\n';
j2 = '        "J2": %.15f,\n';
j3 = '        "J3": %.15f,\n';
j4 = '        "J4": %.15f,\n';
j5 = '        "J5": %.15f,\n';
j6 = '        "J6": %.15f\n';

fprintf(file, '[\n');
for i = 1:size(J1)
    fprintf(file, '    {\n');
    fprintf(file, j1, trajectory(i, 1));
    fprintf(file, j2, trajectory(i, 2));
    fprintf(file, j3, trajectory(i, 3));
    fprintf(file, j4, trajectory(i, 4));
    fprintf(file, j5, trajectory(i, 5));
    fprintf(file, j6, trajectory(i, 6));
    fprintf(file, '    },\n');
end
fprintf(file, ']\n');

fclose(file);


