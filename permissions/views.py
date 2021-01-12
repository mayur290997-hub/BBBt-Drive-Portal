from django.shortcuts import render
from Files.models import Files
from account.models import Member
from permissions.models import Permission
# Create your views here.

def shared_file_per(request,pk):
    file_object=Files.objects.get(pk=pk)
    data_dict={'file_object':file_object}
    return render(request, "Files/shared_file.html",data_dict)

def share(request,pk):
    if request.method == "POST":
        member_object=request.POST['username']
        member=Member.Objects.get(pk=member_object)
        permission_object=Permission.objects.create(file_object=file_object,
                                                    member_object=member_object,
                                                    )
        return HttpResponseRedirect(reverse('Files:shared_file'))
    return render(request, "Files/shared_file.html")