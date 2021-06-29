function f = Analogos(x,Train,Test)
%
%x vector de enteros representando la selección de puntos.
%Train tramo de la matriz para entrenar.
%Test tramo de la matriz para la validación.
%
m = reshape(sum(abs(repmat(Train(x,:),1, size(Test,2))-repelem(Test(x,:), 1, size(Train, 2)))), size(Train,2),size(Test,2));
[~,p] = sort(m,'ascend');
e = sum(sum((Test-0.5*(Train(:,p(1,:)')+Train(:,p(2,:)'))).^2));
f=sqrt(e/(size(Test,1)*size(Test,2)));


