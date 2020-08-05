-- =============================================
-- Author:    Eli Algranti
-- Description:  Standard Normal Distribution 
--        Cumulative Distribution Function
--        using a rational polynomial 
--        approximation to erf() from
--        W. J. Cody 1969
-- Copyright:  Eli Algranti (c) 2012
--
-- This code is licensed under the Microsoft Public 
-- License (Ms-Pl) (http://tsqlnormdist.codeplex.com/license)
-- =============================================
CREATE FUNCTION [dbo].[StdNormalDistributionCDF_3] ( @x FLOAT)
RETURNS FLOAT
AS
    BEGIN
    DECLARE @Z FLOAT = ABS(@x)/SQRT(2.0);
    DECLARE @Z2 FLOAT = @Z*@Z; -- optimization
    
    IF (@Z >=11.0) -- value is too large no need to compute
    BEGIN
      IF @x > 0.0
        RETURN 1.0;
      RETURN 0.0;
    END

    -- Compute ERF using W. J. Cody 1969
    
    DECLARE @ERF FLOAT;
    
    IF (@Z <= 0.46786)
    BEGIN
      DECLARE @pA0 FLOAT = 3.209377589138469472562E03;
      DECLARE @pA1 FLOAT = 3.774852376853020208137E02;
      DECLARE @pA2 FLOAT = 1.138641541510501556495E02;
      DECLARE @pA3 FLOAT = 3.161123743870565596947E00;
      DECLARE @pA4 FLOAT = 1.857777061846031526730E-01;
      
      DECLARE @qA0 FLOAT = 2.844236833439170622273E03;
      DECLARE @qA1 FLOAT = 1.282616526077372275645E03;
      DECLARE @qA2 FLOAT = 2.440246379344441733056E02;
      DECLARE @qA3 FLOAT = 2.360129095234412093499E01;
      DECLARE @qA4 FLOAT = 1.000000000000000000000E00;

      -- For efficiency compute sequence of powers of @Z 
      -- (instead of calling POWER(@Z,2), POWER(@Z,4), etc.)
      DECLARE @ZA4 FLOAT = @Z2*@Z2;
      DECLARE @ZA6 FLOAT = @ZA4*@Z2;
      DECLARE @ZA8 FLOAT = @ZA6*@Z2;


      SELECT @ERF = @Z *
        (@pA0 + @pA1*@Z2 + @pA2*@ZA4 + @pA3*@ZA6 + @pA4*@ZA8) /
        (@qA0 + @qA1*@Z2 + @qA2*@ZA4 + @qA3*@ZA6 + @qA4*@ZA8);
    END
    ELSE IF (@Z <= 4.0)
    BEGIN
      DECLARE @pB0 FLOAT = 1.23033935479799725272E03;
      DECLARE @pB1 FLOAT = 2.05107837782607146532E03;
      DECLARE @pB2 FLOAT = 1.71204761263407058314E03;
      DECLARE @pB3 FLOAT = 8.81952221241769090411E02;
      DECLARE @pB4 FLOAT = 2.98635138197400131132E02;
      DECLARE @pB5 FLOAT = 6.61191906371416294775E01;
      DECLARE @pB6 FLOAT = 8.88314979438837594118E00;
      DECLARE @pB7 FLOAT = 5.64188496988670089180E-01;
      DECLARE @pB8 FLOAT = 2.15311535474403846343E-08;
      
      DECLARE @qB0 FLOAT = 1.23033935480374942043E03;
      DECLARE @qB1 FLOAT = 3.43936767414372163696E03;
      DECLARE @qB2 FLOAT = 4.36261909014324715820E03;
      DECLARE @qB3 FLOAT = 3.29079923573345962678E03;
      DECLARE @qB4 FLOAT = 1.62138957456669018874E03;
      DECLARE @qB5 FLOAT = 5.37181101862009857509E02;
      DECLARE @qB6 FLOAT = 1.17693950891312499305E02;
      DECLARE @qB7 FLOAT = 1.57449261107098347253E01;
      DECLARE @qB8 FLOAT = 1.00000000000000000000E00;

      -- For efficiency compute sequence of powers of @Z 
      -- (instead of calling POWER(@Z,2), POWER(@Z,3), etc.)
      DECLARE @ZB3 FLOAT = @Z2*@Z;
      DECLARE @ZB4 FLOAT = @ZB3*@Z;
      DECLARE @ZB5 FLOAT = @ZB4*@Z;
      DECLARE @ZB6 FLOAT = @ZB5*@Z;
      DECLARE @ZB7 FLOAT = @ZB6*@Z;
      DECLARE @ZB8 FLOAT = @ZB7*@Z;

      SELECT @ERF = 1.0 - EXP(-@Z2) *
              (@pB0 + @pB1*@Z + @pB2*@Z2 + @pB3*@ZB3 + @pB4*@ZB4
               + @pB5*@ZB5 + @pB6*@ZB6 + @pB7*@ZB7 + @pB8*@ZB8) /
              (@qB0 + @qB1*@Z + @qB2*@Z2 + @qB3*@ZB3 + @qB4*@ZB4
               + @qB5*@ZB5 + @qB6*@ZB6 + @qB7*@ZB7 + @qB8*@ZB8);
    END
    ELSE
    BEGIN
      DECLARE @pC0 FLOAT = -6.58749161529837803157E-04;
      DECLARE @pC1 FLOAT = -1.60837851487422766278E-02;
      DECLARE @pC2 FLOAT = -1.25781726111229246204E-01;
      DECLARE @pC3 FLOAT = -3.60344899949804439429E-01;
      DECLARE @pC4 FLOAT = -3.05326634961232344035E-01;
      DECLARE @pC5 FLOAT = -1.63153871373020978498E-02;
      
      DECLARE @qC0 FLOAT = 2.33520497626869185443E-03;
      DECLARE @qC1 FLOAT = 6.05183413124413191178E-02;
      DECLARE @qC2 FLOAT = 5.27905102951428412248E-01;
      DECLARE @qC3 FLOAT = 1.87295284992346047209E00;
      DECLARE @qC4 FLOAT = 2.56852019228982242072E00;
      DECLARE @qC5 FLOAT = 1.00000000000000000000E00;
      
      DECLARE @pi FLOAT = 3.141592653589793238462643383;
      
      -- For efficiency compute sequence of powers of @Z 
      -- (instead of calling POWER(@Z,-2), POWER(@Z,-3), etc.)
      DECLARE @ZC2 FLOAT = (1/@Z)/@Z;
      DECLARE @ZC4 FLOAT = @ZC2*@ZC2;
      DECLARE @ZC6 FLOAT = @ZC4*@ZC2;
      DECLARE @ZC8 FLOAT = @ZC6*@ZC2;
      DECLARE @ZC10 FLOAT = @ZC8*@ZC2;

      SELECT @ERF = 1 - EXP(-@Z2)/@Z * (1/SQRT(@pi) + 1/(@Z2)*
             ((@pC0 + @pC1*@ZC2 + @pC2*@ZC4 + @pC3*@ZC6 + @pC4*@ZC8 + @pC5*@ZC10) /
              (@qC0 + @qC1*@ZC2 + @qC2*@ZC4 + @qC3*@ZC6 + @qC4*@ZC8 + @qC5*@ZC10)));
    END

    DECLARE @cd FLOAT = 0.5*(1+@ERF);

    IF @x > 0
      RETURN @cd;

    RETURN 1.0-@cd;
    END
GO

CREATE FUNCTION dbo.NORMAL_CDF
(
    @X          FLOAT       -- Point at which function is to be evaluated
    ,@Mean      FLOAT       -- Mean of the Normal Distribution
    ,@StdDev    FLOAT       -- Standard Deviation of the Normal Distribution
)	
RETURNS FLOAT(10)
AS
BEGIN
		RETURN [dbo].[Stdnormaldistributioncdf_3]((@X-@Mean) / @StdDev)
END
GO

create table tbC2Inew(
   SCELL                nvarchar(50)        not null,
   NCELL                nvarchar(50)        not null,
   C2I_Mean             float                null,
   Std                  float                null,
   PrbC2I9              float                null,
   PrbABS6              float                null,
   primary key (SCELL, NCELL)
)
go

create table tbC2I3(
   CELL1                nvarchar(50)        not null,
   CELL2                nvarchar(50)        not null,
   CELL3                nvarchar(50)        not null,
   primary key (CELL1, CELL2, CELL3)
)
go

create procedure generate_triSector @rate float
as
	begin
		with bisector as(
			select SCELL,NCELL
			from tbC2Inew
			where PrbABS6>@rate
			union
			select NCELL,SCELL
			from tbC2Inew
			where PrbABS6>@rate
		)
      insert into tbC2I3
   		select distinct a.SCELL,a.NCELL,b.SCELL
	   	from bisector as a,bisector as b
		   where a.SCELL=b.NCELL and a.SCELL<>b.SCELL and a.SCELL>a.NCELL and a.NCELL>b.SCELL
	end
go

create procedure C2I_Analyse @minimum int
as
begin
    delete from tbC2Inew
	insert into tbC2Inew
	    select ServingSector,InterferingSector, C2I_mean, Std, [dbo].[NORMAL_CDF](9, C2I_Mean, Std) as PrbC2I9,[dbo].[NORMAL_CDF](6, C2I_Mean, Std)-[dbo].[NORMAL_CDF](-6, C2I_Mean, Std) as PrbABS6 
		from(
			select ServingSector,InterferingSector,avg(C2I) as C2I_mean,stdev(C2I) as Std
			from(
                    select ServingSector,InterferingSector,(LteScRSRP-LteNcRSRP)as C2I 
                    from tbMROData as t
                    where (ServingSector+'to'+InterferingSector) in(
                    select ServingSector+'to'+InterferingSector as sectors
                    from tbMROData as b
                    group by ServingSector,InterferingSector 
                    having count(*)>=@minimum
				)
			) as a
			group by ServingSector,InterferingSector) as b
end
go


INSERT  INTO [tbPRBnew] 
select [c].[起始时间],[周期],[网元名称],[小区],[b].[小区名],
    [第0个prb上检测到的干扰噪声的平均值_field], [第1个prb上检测到的干扰噪声的平均值_field], [第2个prb上检测到的干扰噪声的平均值_field], [第3个prb上检测到的干扰噪声的平均值_field], [第4个prb上检测到的干扰噪声的平均值_field], [第5个prb上检测到的干扰噪声的平均值_field], [第6个prb上检测到的干扰噪声的平均值_field], [第7个prb上检测到的干扰噪声的平均值_field], [第8个prb上检测到的干扰噪声的平均值_field], [第9个prb上检测到的干扰噪声的平均值_field],
    [第10个prb上检测到的干扰噪声的平均值_field], [第11个prb上检测到的干扰噪声的平均值_field], [第12个prb上检测到的干扰噪声的平均值_field], [第13个prb上检测到的干扰噪声的平均值_field], [第14个prb上检测到的干扰噪声的平均值_field], [第15个prb上检测到的干扰噪声的平均值_field], [第16个prb上检测到的干扰噪声的平均值_field], [第17个prb上检测到的干扰噪声的平均值_field], [第18个prb上检测到的干扰噪声的平均值_field], [第19个prb上检测到的干扰噪声的平均值_field],
    [第20个prb上检测到的干扰噪声的平均值_field], [第21个prb上检测到的干扰噪声的平均值_field], [第22个prb上检测到的干扰噪声的平均值_field], [第23个prb上检测到的干扰噪声的平均值_field], [第24个prb上检测到的干扰噪声的平均值_field], [第25个prb上检测到的干扰噪声的平均值_field], [第26个prb上检测到的干扰噪声的平均值_field], [第27个prb上检测到的干扰噪声的平均值_field], [第28个prb上检测到的干扰噪声的平均值_field], [第29个prb上检测到的干扰噪声的平均值_field],
    [第30个prb上检测到的干扰噪声的平均值_field], [第31个prb上检测到的干扰噪声的平均值_field], [第32个prb上检测到的干扰噪声的平均值_field], [第33个prb上检测到的干扰噪声的平均值_field], [第34个prb上检测到的干扰噪声的平均值_field], [第35个prb上检测到的干扰噪声的平均值_field], [第36个prb上检测到的干扰噪声的平均值_field], [第37个prb上检测到的干扰噪声的平均值_field], [第38个prb上检测到的干扰噪声的平均值_field], [第39个prb上检测到的干扰噪声的平均值_field],
    [第40个prb上检测到的干扰噪声的平均值_field], [第41个prb上检测到的干扰噪声的平均值_field], [第42个prb上检测到的干扰噪声的平均值_field], [第43个prb上检测到的干扰噪声的平均值_field], [第44个prb上检测到的干扰噪声的平均值_field], [第45个prb上检测到的干扰噪声的平均值_field], [第46个prb上检测到的干扰噪声的平均值_field], [第47个prb上检测到的干扰噪声的平均值_field], [第48个prb上检测到的干扰噪声的平均值_field], [第49个prb上检测到的干扰噪声的平均值_field],
    [第50个prb上检测到的干扰噪声的平均值_field], [第51个prb上检测到的干扰噪声的平均值_field], [第52个prb上检测到的干扰噪声的平均值_field], [第53个prb上检测到的干扰噪声的平均值_field], [第54个prb上检测到的干扰噪声的平均值_field], [第55个prb上检测到的干扰噪声的平均值_field], [第56个prb上检测到的干扰噪声的平均值_field], [第57个prb上检测到的干扰噪声的平均值_field], [第58个prb上检测到的干扰噪声的平均值_field], [第59个prb上检测到的干扰噪声的平均值_field],
    [第60个prb上检测到的干扰噪声的平均值_field], [第61个prb上检测到的干扰噪声的平均值_field], [第62个prb上检测到的干扰噪声的平均值_field], [第63个prb上检测到的干扰噪声的平均值_field], [第64个prb上检测到的干扰噪声的平均值_field], [第65个prb上检测到的干扰噪声的平均值_field], [第66个prb上检测到的干扰噪声的平均值_field], [第67个prb上检测到的干扰噪声的平均值_field], [第68个prb上检测到的干扰噪声的平均值_field], [第69个prb上检测到的干扰噪声的平均值_field],
    [第70个prb上检测到的干扰噪声的平均值_field], [第71个prb上检测到的干扰噪声的平均值_field], [第72个prb上检测到的干扰噪声的平均值_field], [第73个prb上检测到的干扰噪声的平均值_field], [第74个prb上检测到的干扰噪声的平均值_field], [第75个prb上检测到的干扰噪声的平均值_field], [第76个prb上检测到的干扰噪声的平均值_field], [第77个prb上检测到的干扰噪声的平均值_field], [第78个prb上检测到的干扰噪声的平均值_field], [第79个prb上检测到的干扰噪声的平均值_field],
    [第80个prb上检测到的干扰噪声的平均值_field], [第81个prb上检测到的干扰噪声的平均值_field], [第82个prb上检测到的干扰噪声的平均值_field], [第83个prb上检测到的干扰噪声的平均值_field], [第84个prb上检测到的干扰噪声的平均值_field], [第85个prb上检测到的干扰噪声的平均值_field], [第86个prb上检测到的干扰噪声的平均值_field], [第87个prb上检测到的干扰噪声的平均值_field], [第88个prb上检测到的干扰噪声的平均值_field], [第89个prb上检测到的干扰噪声的平均值_field],
    [第90个prb上检测到的干扰噪声的平均值_field], [第91个prb上检测到的干扰噪声的平均值_field], [第92个prb上检测到的干扰噪声的平均值_field], [第93个prb上检测到的干扰噪声的平均值_field], [第94个prb上检测到的干扰噪声的平均值_field], [第95个prb上检测到的干扰噪声的平均值_field], [第96个prb上检测到的干扰噪声的平均值_field], [第97个prb上检测到的干扰噪声的平均值_field], [第98个prb上检测到的干扰噪声的平均值_field], [第99个prb上检测到的干扰噪声的平均值_field]
from(
        select [小区名],	DATEPART(HOUR,[起始时间]) as hour,DATEPART(DAY,[起始时间])as day,DATEPART(MONTH,[起始时间])as month,DATEPART(YEAR,[起始时间]) as year,
            avg([第0个prb上检测到的干扰噪声的平均值_field]) as [第0个prb上检测到的干扰噪声的平均值_field], avg([第1个prb上检测到的干扰噪声的平均值_field]) as [第1个prb上检测到的干扰噪声的平均值_field], avg([第2个prb上检测到的干扰噪声的平均值_field]) as [第2个prb上检测到的干扰噪声的平均值_field], avg([第3个prb上检测到的干扰噪声的平均值_field]) as [第3个prb上检测到的干扰噪声的平均值_field], avg([第4个prb上检测到的干扰噪声的平均值_field]) as [第4个prb上检测到的干扰噪声的平均值_field], avg([第5个prb上检测到的干扰噪声的平均值_field]) as [第5个prb上检测到的干扰噪声的平均值_field], avg([第6个prb上检测到的干扰噪声的平均值_field]) as [第6个prb上检测到的干扰噪声的平均值_field], avg([第7个prb上检测到的干扰噪声的平均值_field]) as [第7个prb上检测到的干扰噪声的平均值_field], avg([第8个prb上检测到的干扰噪声的平均值_field]) as [第8个prb上检测到的干扰噪声的平均值_field], avg([第9个prb上检测到的干扰噪声的平均值_field]) as [第9个prb上检测到的干扰噪声的平均值_field], 
            avg([第10个prb上检测到的干扰噪声的平均值_field]) as [第10个prb上检测到的干扰噪声的平均值_field], avg([第11个prb上检测到的干扰噪声的平均值_field]) as [第11个prb上检测到的干扰噪声的平均值_field], avg([第12个prb上检测到的干扰噪声的平均值_field]) as [第12个prb上检测到的干扰噪声的平均值_field], avg([第13个prb上检测到的干扰噪声的平均值_field]) as [第13个prb上检测到的干扰噪声的平均值_field], avg([第14个prb上检测到的干扰噪声的平均值_field]) as [第14个prb上检测到的干扰噪声的平均值_field], avg([第15个prb上检测到的干扰噪声的平均值_field]) as [第15个prb上检测到的干扰噪声的平均值_field], avg([第16个prb上检测到的干扰噪声的平均值_field]) as [第16个prb上检测到的干扰噪声的平均值_field], avg([第17个prb上检测到的干扰噪声的平均值_field]) as [第17个prb上检测到的干扰噪声的平均值_field], avg([第18个prb上检测到的干扰噪声的平均值_field]) as [第18个prb上检测到的干扰噪声的平均值_field], avg([第19个prb上检测到的干扰噪声的平均值_field]) as [第19个prb上检测到的干扰噪声的平均值_field], 
            avg([第20个prb上检测到的干扰噪声的平均值_field]) as [第20个prb上检测到的干扰噪声的平均值_field], avg([第21个prb上检测到的干扰噪声的平均值_field]) as [第21个prb上检测到的干扰噪声的平均值_field], avg([第22个prb上检测到的干扰噪声的平均值_field]) as [第22个prb上检测到的干扰噪声的平均值_field], avg([第23个prb上检测到的干扰噪声的平均值_field]) as [第23个prb上检测到的干扰噪声的平均值_field], avg([第24个prb上检测到的干扰噪声的平均值_field]) as [第24个prb上检测到的干扰噪声的平均值_field], avg([第25个prb上检测到的干扰噪声的平均值_field]) as [第25个prb上检测到的干扰噪声的平均值_field], avg([第26个prb上检测到的干扰噪声的平均值_field]) as [第26个prb上检测到的干扰噪声的平均值_field], avg([第27个prb上检测到的干扰噪声的平均值_field]) as [第27个prb上检测到的干扰噪声的平均值_field], avg([第28个prb上检测到的干扰噪声的平均值_field]) as [第28个prb上检测到的干扰噪声的平均值_field], avg([第29个prb上检测到的干扰噪声的平均值_field]) as [第29个prb上检测到的干扰噪声的平均值_field], 
            avg([第30个prb上检测到的干扰噪声的平均值_field]) as [第30个prb上检测到的干扰噪声的平均值_field], avg([第31个prb上检测到的干扰噪声的平均值_field]) as [第31个prb上检测到的干扰噪声的平均值_field], avg([第32个prb上检测到的干扰噪声的平均值_field]) as [第32个prb上检测到的干扰噪声的平均值_field], avg([第33个prb上检测到的干扰噪声的平均值_field]) as [第33个prb上检测到的干扰噪声的平均值_field], avg([第34个prb上检测到的干扰噪声的平均值_field]) as [第34个prb上检测到的干扰噪声的平均值_field], avg([第35个prb上检测到的干扰噪声的平均值_field]) as [第35个prb上检测到的干扰噪声的平均值_field], avg([第36个prb上检测到的干扰噪声的平均值_field]) as [第36个prb上检测到的干扰噪声的平均值_field], avg([第37个prb上检测到的干扰噪声的平均值_field]) as [第37个prb上检测到的干扰噪声的平均值_field], avg([第38个prb上检测到的干扰噪声的平均值_field]) as [第38个prb上检测到的干扰噪声的平均值_field], avg([第39个prb上检测到的干扰噪声的平均值_field]) as [第39个prb上检测到的干扰噪声的平均值_field], 
            avg([第40个prb上检测到的干扰噪声的平均值_field]) as [第40个prb上检测到的干扰噪声的平均值_field], avg([第41个prb上检测到的干扰噪声的平均值_field]) as [第41个prb上检测到的干扰噪声的平均值_field], avg([第42个prb上检测到的干扰噪声的平均值_field]) as [第42个prb上检测到的干扰噪声的平均值_field], avg([第43个prb上检测到的干扰噪声的平均值_field]) as [第43个prb上检测到的干扰噪声的平均值_field], avg([第44个prb上检测到的干扰噪声的平均值_field]) as [第44个prb上检测到的干扰噪声的平均值_field], avg([第45个prb上检测到的干扰噪声的平均值_field]) as [第45个prb上检测到的干扰噪声的平均值_field], avg([第46个prb上检测到的干扰噪声的平均值_field]) as [第46个prb上检测到的干扰噪声的平均值_field], avg([第47个prb上检测到的干扰噪声的平均值_field]) as [第47个prb上检测到的干扰噪声的平均值_field], avg([第48个prb上检测到的干扰噪声的平均值_field]) as [第48个prb上检测到的干扰噪声的平均值_field], avg([第49个prb上检测到的干扰噪声的平均值_field]) as [第49个prb上检测到的干扰噪声的平均值_field], 
            avg([第50个prb上检测到的干扰噪声的平均值_field]) as [第50个prb上检测到的干扰噪声的平均值_field], avg([第51个prb上检测到的干扰噪声的平均值_field]) as [第51个prb上检测到的干扰噪声的平均值_field], avg([第52个prb上检测到的干扰噪声的平均值_field]) as [第52个prb上检测到的干扰噪声的平均值_field], avg([第53个prb上检测到的干扰噪声的平均值_field]) as [第53个prb上检测到的干扰噪声的平均值_field], avg([第54个prb上检测到的干扰噪声的平均值_field]) as [第54个prb上检测到的干扰噪声的平均值_field], avg([第55个prb上检测到的干扰噪声的平均值_field]) as [第55个prb上检测到的干扰噪声的平均值_field], avg([第56个prb上检测到的干扰噪声的平均值_field]) as [第56个prb上检测到的干扰噪声的平均值_field], avg([第57个prb上检测到的干扰噪声的平均值_field]) as [第57个prb上检测到的干扰噪声的平均值_field], avg([第58个prb上检测到的干扰噪声的平均值_field]) as [第58个prb上检测到的干扰噪声的平均值_field], avg([第59个prb上检测到的干扰噪声的平均值_field]) as [第59个prb上检测到的干扰噪声的平均值_field], 
            avg([第60个prb上检测到的干扰噪声的平均值_field]) as [第60个prb上检测到的干扰噪声的平均值_field], avg([第61个prb上检测到的干扰噪声的平均值_field]) as [第61个prb上检测到的干扰噪声的平均值_field], avg([第62个prb上检测到的干扰噪声的平均值_field]) as [第62个prb上检测到的干扰噪声的平均值_field], avg([第63个prb上检测到的干扰噪声的平均值_field]) as [第63个prb上检测到的干扰噪声的平均值_field], avg([第64个prb上检测到的干扰噪声的平均值_field]) as [第64个prb上检测到的干扰噪声的平均值_field], avg([第65个prb上检测到的干扰噪声的平均值_field]) as [第65个prb上检测到的干扰噪声的平均值_field], avg([第66个prb上检测到的干扰噪声的平均值_field]) as [第66个prb上检测到的干扰噪声的平均值_field], avg([第67个prb上检测到的干扰噪声的平均值_field]) as [第67个prb上检测到的干扰噪声的平均值_field], avg([第68个prb上检测到的干扰噪声的平均值_field]) as [第68个prb上检测到的干扰噪声的平均值_field], avg([第69个prb上检测到的干扰噪声的平均值_field]) as [第69个prb上检测到的干扰噪声的平均值_field], 
            avg([第70个prb上检测到的干扰噪声的平均值_field]) as [第70个prb上检测到的干扰噪声的平均值_field], avg([第71个prb上检测到的干扰噪声的平均值_field]) as [第71个prb上检测到的干扰噪声的平均值_field], avg([第72个prb上检测到的干扰噪声的平均值_field]) as [第72个prb上检测到的干扰噪声的平均值_field], avg([第73个prb上检测到的干扰噪声的平均值_field]) as [第73个prb上检测到的干扰噪声的平均值_field], avg([第74个prb上检测到的干扰噪声的平均值_field]) as [第74个prb上检测到的干扰噪声的平均值_field], avg([第75个prb上检测到的干扰噪声的平均值_field]) as [第75个prb上检测到的干扰噪声的平均值_field], avg([第76个prb上检测到的干扰噪声的平均值_field]) as [第76个prb上检测到的干扰噪声的平均值_field], avg([第77个prb上检测到的干扰噪声的平均值_field]) as [第77个prb上检测到的干扰噪声的平均值_field], avg([第78个prb上检测到的干扰噪声的平均值_field]) as [第78个prb上检测到的干扰噪声的平均值_field], avg([第79个prb上检测到的干扰噪声的平均值_field]) as [第79个prb上检测到的干扰噪声的平均值_field], 
            avg([第80个prb上检测到的干扰噪声的平均值_field]) as [第80个prb上检测到的干扰噪声的平均值_field], avg([第81个prb上检测到的干扰噪声的平均值_field]) as [第81个prb上检测到的干扰噪声的平均值_field], avg([第82个prb上检测到的干扰噪声的平均值_field]) as [第82个prb上检测到的干扰噪声的平均值_field], avg([第83个prb上检测到的干扰噪声的平均值_field]) as [第83个prb上检测到的干扰噪声的平均值_field], avg([第84个prb上检测到的干扰噪声的平均值_field]) as [第84个prb上检测到的干扰噪声的平均值_field], avg([第85个prb上检测到的干扰噪声的平均值_field]) as [第85个prb上检测到的干扰噪声的平均值_field], avg([第86个prb上检测到的干扰噪声的平均值_field]) as [第86个prb上检测到的干扰噪声的平均值_field], avg([第87个prb上检测到的干扰噪声的平均值_field]) as [第87个prb上检测到的干扰噪声的平均值_field], avg([第88个prb上检测到的干扰噪声的平均值_field]) as [第88个prb上检测到的干扰噪声的平均值_field], avg([第89个prb上检测到的干扰噪声的平均值_field]) as [第89个prb上检测到的干扰噪声的平均值_field], 
            avg([第90个prb上检测到的干扰噪声的平均值_field]) as [第90个prb上检测到的干扰噪声的平均值_field], avg([第91个prb上检测到的干扰噪声的平均值_field]) as [第91个prb上检测到的干扰噪声的平均值_field], avg([第92个prb上检测到的干扰噪声的平均值_field]) as [第92个prb上检测到的干扰噪声的平均值_field], avg([第93个prb上检测到的干扰噪声的平均值_field]) as [第93个prb上检测到的干扰噪声的平均值_field], avg([第94个prb上检测到的干扰噪声的平均值_field]) as [第94个prb上检测到的干扰噪声的平均值_field], avg([第95个prb上检测到的干扰噪声的平均值_field]) as [第95个prb上检测到的干扰噪声的平均值_field], avg([第96个prb上检测到的干扰噪声的平均值_field]) as [第96个prb上检测到的干扰噪声的平均值_field], avg([第97个prb上检测到的干扰噪声的平均值_field]) as [第97个prb上检测到的干扰噪声的平均值_field], avg([第98个prb上检测到的干扰噪声的平均值_field]) as [第98个prb上检测到的干扰噪声的平均值_field], avg([第99个prb上检测到的干扰噪声的平均值_field]) as [第99个prb上检测到的干扰噪声的平均值_field]
        from [tbPRB]
        group by DATEPART(HOUR,[起始时间]),DATEPART(DAY,[起始时间]),DATEPART(MONTH,[起始时间]),DATEPART(YEAR,[起始时间]),[小区名]
     )
		 as [b],
		 (select [起始时间],[周期],[网元名称],[小区],[小区名] from [tbPRB]) as [c]
    where  DATEPART(MINUTE, [c].[起始时间])=0 and hour=DATEPART(HOUR,[c].[起始时间]) and day=DATEPART(DAY,[c].[起始时间])  and [b].[小区名]=[c].[小区名];
