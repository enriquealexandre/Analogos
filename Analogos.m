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


%Código menos eficiente pero más legible:
% function [f]=Analogos(x,Train,Test)
% %
% e=zeros(size(Test,2),1);
% for i=1:size(Test,2) 
%   M=abs(Train(x,:)-Test(x,i)*ones(1,size(Train,2))); 
%   m=sum(M); 
%   [k,p]=sort(m,'ascend'); 
%   b=[p(1) p(2)];
%   T=0.5*(Train(:,b(1))+Train(:,b(2))); 
%   e(i)=sum((T-Test(:,i)).^2);           
% end
% e
% f=sum(e)/length(e)